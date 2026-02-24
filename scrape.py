import os
import requests
import html as html_lib
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Configuration
BASE_URL = "https://barbershop.framer.website/"
OUTPUT_DIR = "/home/matheusht/Documents/github/bladebarber"
PUBLIC_DIR = os.path.join(OUTPUT_DIR, "public")
ASSETS_DIR = os.path.join(PUBLIC_DIR, "assets")

os.makedirs(ASSETS_DIR, exist_ok=True)

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})

def download_asset(url):
    if not url: return url
    url = html_lib.unescape(url)
    
    # Skip non-http URLs
    if any(url.startswith(p) for p in ['data:', '#', 'javascript:', 'tel:', 'mailto:']):
        return url
        
    if url.startswith('//'):
        url = 'https:' + url
        
    parsed = urlparse(url)
    if not parsed.netloc:
        url = urljoin(BASE_URL, url)
        parsed = urlparse(url)
        
    # Generate a safe filename
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        # Fallback for paths without extension or query params
        import hashlib
        ext = ".png" # default
        if "woff2" in url: ext = ".woff2"
        elif "woff" in url: ext = ".woff"
        elif "css" in url: ext = ".css"
        elif "js" in url: ext = ".js"
        filename = hashlib.md5(url.encode()).hexdigest() + ext
    else:
        # Keep extension but sanitise name
        name_parts = os.path.splitext(filename)
        filename = "".join(x for x in name_parts[0] if x.isalnum() or x in "._-") + name_parts[1]
    
    local_path = os.path.join(ASSETS_DIR, filename)
    asset_rel_path = f"/assets/{filename}"
    
    if os.path.exists(local_path):
        return asset_rel_path
        
    print(f"Downloading: {url}")
    try:
        r = session.get(url, timeout=15)
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            f.write(r.content)
        return asset_rel_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return url

def process_css(css_content, base_url):
    import re
    def rel_to_abs_css(m):
        u = m.group(2).strip("'\"").strip()
        if not u or any(u.startswith(p) for p in ['data:', '#', 'javascript:', 'tel:', 'mailto:']):
            return m.group(0)
        abs_u = urljoin(base_url, u)
        return f"url('{download_asset(abs_u)}')"
    
    # More robust URL matching to avoid unclosed strings
    return re.sub(r'url\(([\'"]?)(.+?)\1\)', rel_to_abs_css, css_content)

def scrape_page(path):
    url = urljoin(BASE_URL, path)
    print(f"Scraping {url}...")
    try:
        r = session.get(url, timeout=20)
        r.raise_for_status()
        html = r.content.decode('utf-8', errors='replace')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return

    html = html.replace('â€', "'").replace('â€œ', '"').replace('â€\x9d', '"').replace('â€™', "'")
    soup = BeautifulSoup(html, 'html.parser')

    # 1. Process Links and Scripts
    for tag in soup.find_all(['link', 'script', 'img', 'source', 'video', 'embed', 'iframe']):
        for attr in ['src', 'href', 'data-src', 'poster', 'srcset']:
            if tag.has_attr(attr):
                val = tag[attr]
                if attr == 'srcset':
                    parts = []
                    for s in val.split(','):
                        s = s.strip()
                        if not s: continue
                        bits = s.split()
                        try:
                            bits[0] = download_asset(urljoin(BASE_URL, bits[0]))
                            parts.append(" ".join(bits))
                        except: pass
                    tag[attr] = ", ".join(parts)
                else:
                    tag[attr] = download_asset(urljoin(BASE_URL, val))

    # 2. Process Style Tags
    for style in soup.find_all('style'):
        if style.string:
            style.string = process_css(style.string, url)

    # 3. Process Inline Styles
    for tag in soup.find_all(style=True):
        tag['style'] = process_css(tag['style'], url)

    # 4. Handle internal links
    for a in soup.find_all('a', href=True):
        href = a['href']
        # Map internal Framer pages to local .html files
        abs_href = urljoin(BASE_URL, href).split('?')[0].split('#')[0].rstrip('/')
        
        target_paths = {
            BASE_URL.rstrip('/'): "/",
            urljoin(BASE_URL, "about").rstrip('/'): "/about.html",
            urljoin(BASE_URL, "services").rstrip('/'): "/services.html",
            urljoin(BASE_URL, "contact").rstrip('/'): "/contact.html",
            urljoin(BASE_URL, "gallery").rstrip('/'): "/gallery.html",
        }
        
        if abs_href in target_paths:
            a['href'] = target_paths[abs_href]

    # 5. Clean up problematic comments
    for comment in soup.find_all(string=lambda text: isinstance(text, (str, type(soup.new_string("")))) and ("Built with Framer" in text or "Start of" in text or "End of" in text)):
        comment.extract()

    # 6. Inject Vite module script
    vite_script = soup.new_tag('script', type='module', src='/src/main.js')
    if soup.body:
        soup.body.append(vite_script)
    else:
        soup.append(vite_script)

    # Final HTML generation
    content = soup.encode(formatter="html").decode('utf-8')
    content = "".join(c if ord(c) < 128 else f"&#{ord(c)};" for c in content)

    filename = "index.html" if not path else f"{path.strip('/')}.html"
    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Scraped {path} to {filename}")

def main():
    paths = ['', 'about', 'services', 'contact', 'gallery']
    for p in paths:
        scrape_page(p)
    print("Multi-page scrape complete!")

if __name__ == "__main__":
    main()
