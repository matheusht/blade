import os

translations = {
    '"Home"': '"Início"',
    '`Home`': '`Início`',
    '>Home<': '>Início<',
    '"About Us"': '"Sobre Nós"',
    '`About Us`': '`Sobre Nós`',
    '>About Us<': '>Sobre Nós<',
    '>About us<': '>Sobre Nós<',
    '`About us`': '`Sobre Nós`',
    '"Pricing"': '"Preços"',
    '`Pricing`': '`Preços`',
    '>Pricing<': '>Preços<',
    '"Services"': '"Serviços"',
    '`Services`': '`Serviços`',
    '>Services<': '>Serviços<',
    '"Gallery"': '"Galeria"',
    '`Gallery`': '`Galeria`',
    '>Gallery<': '>Galeria<',
    '"Blog"': '"Blog"',
    '`Blog`': '`Blog`',
    '>Blog<': '>Blog<',
    '"Contact us"': '"Fale Conosco"',
    '`Contact us`': '`Fale Conosco`',
    '>Contact us<': '>Fale Conosco<',
    'BEST MEN’S PARLOUR IN YOUR AREA': 'A MELHOR BARBEARIA DA SUA REGIÃO',
    'BEST MEN\\\'S PARLOUR IN YOUR AREA': 'A MELHOR BARBEARIA DA SUA REGIÃO',
    'Own your style': 'Assuma seu estilo',
    'embrace your power': 'abrace seu poder',
    '"Get Template"': '"Ver Template"',
    '`Get Template`': '`Ver Template`',
    'LOCATION': 'LOCALIZAÇÃO',
    '123 Main Street, Cityville, Stateburg, 98765': '123 Rua Principal, Cidade Velha, Estado Novo, 98765',
    'SEE ON MAP': 'VER NO MAPA',
    'CONTACT': 'CONTATO',
    'OPENING HOURS': 'HORÁRIO DE FUNCIONAMENTO',
    'Mon to Fri: 9.00am - 8.30pm': 'Seg a Sex: 9:00 - 20:30',
    'Sat: 10.00am - 6.30pm': 'Sáb: 10:00 - 18:30',
    'Sun: Closed': 'Dom: Fechado',
    'OUR MAIN SERVICES': 'NOSSOS PRINCIPAIS SERVIÇOS',
    'Our specialities': 'Nossas especialidades',
    'Ultimate grooming for the modern man. Look and feel your best with our skilled stylists and premium products.': 'O melhor cuidado para o homem moderno. Sinta-se e esteja no seu melhor com nossos barbeiros qualificados e produtos premium.',
    'Haircuts & Hairstyling': 'Cortes e Penteados',
    'Haircut & Hairstyling': 'Cortes e Penteados',
    'Beard Styling': 'Estilização de Barba',
    'Grooming & Skincare': 'Cuidados e Skincare',
    'Grooming and Skincare': 'Cuidados e Skincare',
    'COLOR & TREATMENT': 'COLORAÇÃO E TRATAMENTO',
    'Color & Treatment': 'Coloração e Tratamento',
    'BROWSE ALL SERVICES': 'VER TODOS OS SERVIÇOS',
    'WHAT WE OFFER': 'O QUE OFERECEMOS',
    'Our Prices': 'Nossos Preços",',
    'Experience luxury grooming with our diverse services designed just for you. Discover clear pricing aligned with the value you get.': 'Experimente o cuidado de luxo com nossos diversos serviços pensados para você. Descubra preços claros e alinhados com o valor que você recebe.',
    'Tailored Haircuts': 'Cortes Personalizados',
    'Modern Fade': 'Fade Moderno',
    'Beard Trim and Sculpt': 'Aparo e Escultura de Barba',
    'Scalp Treatments': 'Tratamentos de Couro Cabeludo',
    'Hair Treatments': 'Tratamentos Capilares',
    'WHAT CLIENTS SAY': 'O QUE OS CLIENTES DIZEM',
    "Clients\\' feedbacks": "Feedbacks dos clientes",
    "Clients' feedbacks": "Feedbacks dos clientes",
    'See what our clients have to say about their extraordinary experiences at our barber shop. Real stories & real satisfaction.': 'Veja o que nossos clientes têm a dizer sobre suas experiências extraordinárias em nossa barbearia. Histórias reais e satisfação real.',
    'See what our clients have to say about their extraordinary experiences at our barber shop. Real stories &amp; real satisfaction.': 'Veja o que nossos clientes têm a dizer sobre suas experiências extraordinárias em nossa barbearia. Histórias reais e satisfação real.',
    "I\\'ve never felt more confident…": "Nunca me senti tão confiante…",
    "I've never felt more confident…": "Nunca me senti tão confiante…",
    "I've never felt more confident than after getting my haircut at TrimHub Barbershop.": "Nunca me senti tão confiante do que após cortar meu cabelo na Blade Barbearia.",
    "I\\'ve never felt more confident than after getting my haircut at TrimHub Barbershop.": "Nunca me senti tão confiante do que após cortar meu cabelo na Blade Barbearia.",
    "Client, TrimHub Barbershop": "Cliente, Blade Barbearia",
    "exceeded all my expectations...": "superou todas as minhas expectativas...",
    "I was skeptical about trying a new barber shop, but TrimHub Barbershop exceeded all my expectations. The barber took the time to understand my preferences.": "Eu estava cético em relação a tentar uma nova barbearia, mas a Blade Barbearia superou todas as minhas expectativas. O barbeiro dedicou tempo para entender minhas preferências.",
    "an absolute luxury...": "um luxo absoluto...",
    "The hot towel shave was an absolute luxury, and the barber\\'s attention to detail was impressive. The shop\\'s ambiance is inviting, and the staff creates a cozy environment.": "O barbear com toalha quente foi um luxo absoluto, e a atenção do barbeiro aos detalhes foi impressionante. O ambiente da loja é convidativo e a equipe cria um espaço acolhedor.",
    "The hot towel shave was an absolute luxury, and the barber's attention to detail was impressive. The shop's ambiance is inviting, and the staff creates a cozy environment.": "O barbear com toalha quente foi um luxo absoluto, e a atenção do barbeiro aos detalhes foi impressionante. O ambiente da loja é convidativo e a equipe cria um espaço acolhedor.",
    "felt like a work of art.": "parecia uma obra de arte.",
    "The barbers\\' attention to detail and dedication to delivering top-notch cuts is unmatched. I recently tried their grooming service, and I left with a beard that felt like a work of art.": "A atenção dos barbeiros aos detalhes e a dedicação em entregar cortes de alto nível é inigualável. Recentemente experimentei o serviço de grooming e saí com uma barba que parecia uma obra de arte.",
    "The barbers' attention to detail and dedication to delivering top-notch cuts is unmatched. I recently tried their grooming service, and I left with a beard that felt like a work of art.": "A atenção dos barbeiros aos detalhes e a dedicação em entregar cortes de alto nível é inigualável. Recentemente experimentei o serviço de grooming e saí com uma barba que parecia uma obra de arte."
}

sorted_translations = dict(sorted(translations.items(), key=lambda item: len(item[0]), reverse=True))

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for eng, pt in sorted_translations.items():
        content = content.replace(eng, pt)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def main():
    dirs_to_check = ['public', 'dist', 'src']
    for d in dirs_to_check:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for file in files:
                if file.endswith('.mjs') or file.endswith('.js') or file.endswith('.html'):
                    process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
