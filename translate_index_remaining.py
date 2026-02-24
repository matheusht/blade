import os

translations = {
    """Own your style""": """Assuma seu estilo""",
    """own your style""": """assuma seu estilo""",
    """OWN YOUR STYLE""": """ASSUMA SEU ESTILO""",
    """Assuma seu style""": """Assuma seu estilo""",
    """assuma seu style""": """assuma seu estilo""",
    """ASSUMA SEU STYLE""": """ASSUMA SEU ESTILO""",
    """embrace your power""": """abrace seu poder""",
    """Embrace your""": """Abrace seu""",
    """EMBRACE YOUR""": """ABRACE SEU""",
    """power""": """poder""",
    """POWER""": """PODER""",

    """Hot Towel Razor Shave""": """Barbear com Toalha Quente""",
    """HOT TOWEL RAZOR SHAVE""": """BARBEAR COM TOALHA QUENTE""",
    """Executive Grooming""": """Cuidado Executivo""",
    """EXECUTIVE GROOMING""": """CUIDADO EXECUTIVO""",
    """Color and Highlights""": """Coloração e Luzes""",
    """Color & Highlights""": """Coloração e Luzes""",
    """COLOR AND HIGHLIGHTS""": """COLORAÇÃO E LUZES""",
    """Hair Treatment""": """Tratamento Capilar""",
    """HAIR TREATMENT""": """TRATAMENTO CAPILAR""",
    """Refreshing Facial""": """Limpeza de Pele Refrescante""",
    """REFRESHING FACIAL""": """LIMPEZA DE PELE REFRESCANTE""",
    """Hair Color Enhancement""": """Realce de Cor do Cabelo""",
    """HAIR COLOR ENHANCEMENT""": """REALCE DE COR DO CABELO""",
    """Shampoo and Blowout""": """Lavagem e Secagem""",
    """SHAMPOO AND BLOWOUT""": """LAVAGEM E SECAGEM""",
    """Kids' Cut (Under 12)""": """Corte Infantil (menores de 12)""",
    """Kids’ Cut (Under 12)""": """Corte Infantil (menores de 12)""",
    """KIDS' CUT (UNDER 12)""": """CORTE INFANTIL (MENORES DE 12)""",
    """KIDS’ CUT (UNDER 12)""": """CORTE INFANTIL (MENORES DE 12)""",
    """Senior's Special""": """Especial para Idosos""",
    """Senior’s Special""": """Especial para Idosos""",
    """SENIOR'S SPECIAL""": """ESPECIAL PARA IDOSOS""",
    """SENIOR’S SPECIAL""": """ESPECIAL PARA IDOSOS""",
    """Head Shave""": """Raspagem de Cabeça""",
    """HEAD SHAVE""": """RASPAGEM DE CABEÇA""",
    """Custom Consultation""": """Consulta Personalizada""",
    """CUSTOM CONSULTATION""": """CONSULTA PERSONALIZADA""",
    """Free""": """Grátis""",
    """FREE""": """GRÁTIS""",
    """View Detailed Services""": """Ver Serviços Detalhados""",
    """VIEW DETAILED SERVICES""": """VER SERVIÇOS DETALHADOS""",
    """Nossos Preços",""": """Nossos Preços",""",
    
    """Why Choose Our Shop?""": """Por Que Escolher Nossa Barbearia?""",
    """WHY CHOOSE OUR SHOP?""": """POR QUE ESCOLHER NOSSA BARBEARIA?""",
    """Our Differences""": """Nossos Diferenciais""",
    """OUR DIFFERENCES""": """NOSSOS DIFERENCIAIS""",
    """Experience our unique approach to grooming – where personalized service meets skilled artistry. Discover a haven where style and individuality intertwine""": """Experimente nossa abordagem única de cuidados – onde o serviço personalizado encontra a habilidade artística. Descubra um refúgio onde estilo e individualidade se entrelaçam""",
    """Experienced Barbers""": """Barbeiros Experientes""",
    """EXPERIENCED BARBERS""": """BARBEIROS EXPERIENTES""",
    """Relaxing Environment""": """Ambiente Relaxante""",
    """RELAXING ENVIRONMENT""": """AMBIENTE RELAXANTE""",
    """Premium Grooming Products""": """Produtos de Qualidade Premium""",
    """PREMIUM GROOMING PRODUCTS""": """PRODUTOS DE QUALIDADE PREMIUM""",
    """Attention to Detail""": """Atenção aos Detalhes""",
    """Attention To Detail""": """Atenção aos Detalhes""",
    """ATTENTION TO DETAIL""": """ATENÇÃO AOS DETALHES""",

    """Our Story""": """Nossa História""",
    """OUR STORY""": """NOSSA HISTÓRIA""",
    """Est'd 2013""": """Desde 2013""",
    """EST'D 2013""": """DESDE 2013""",
    """Est’d 2013""": """Desde 2013""",
    """EST’D 2013""": """DESDE 2013""",
    """Welcome to TrimHub, where grooming is an art and style is a statement. With a legacy built on tradition and an eye for innovation, we blend classic techniques with modern trends to craft the perfect look for you.""": """Bem-vindo à Blade Barbearia, onde o cuidado é uma arte e o estilo é uma declaração. Com um legado construído na tradição e um olhar para a inovação, misturamos técnicas clássicas com tendências modernas para criar o visual perfeito para você.""",
    """Our team of expert barbers is more than skilled professionals – they're artists who meticulously sculpt each cut and shave with precision. we offer an experience that's as welcoming as it is stylish.""": """Nossa equipe de barbeiros especialistas é mais do que profissionais qualificados – eles são artistas que esculpem meticulosamente cada corte e barba com precisão. Oferecemos uma experiência que é tão acolhedora quanto elegante.""",
    """Our team of expert barbers is more than skilled professionals – they\\'re artists who meticulously sculpt each cut and shave with precision. we offer an experience that\\'s as welcoming as it is stylish.""": """Nossa equipe de barbeiros especialistas é mais do que profissionais qualificados – eles são artistas que esculpem meticulosamente cada corte e barba com precisão. Oferecemos uma experiência que é tão acolhedora quanto elegante.""",
    """-Founder, DrapperCraft Barbers""": """-Fundador, Blade Barbearia""",
    """-FOUNDER, DRAPPERCRAFT BARBERS""": """-FUNDADOR, BLADE BARBEARIA""",
    '"Radiate with Confidence, Like a starlit sky, your skin shines with the brilliance of self-care."': '"Iradie com Confiança. Como um céu estrelado, sua pele brilha com o esplendor do autocuidado."',
    '\\"Radiate with Confidence, Like a starlit sky, your skin shines with the brilliance of self-care.\\"': '\\"Iradie com Confiança. Como um céu estrelado, sua pele brilha com o esplendor do autocuidado.\\"',

    """Latest News""": """Últimas Notícias""",
    """LATEST NEWS""": """ÚLTIMAS NOTÍCIAS""",
    """Discover the Art of grooming, define your signature style, and radiate unparalleled confidence""": """Descubra a Arte do cuidado, defina seu estilo e irradie uma confiança inigualável""",
    """Product Review""": """Revisão de Produtos""",
    """PRODUCT REVIEW""": """REVISÃO DE PRODUTOS""",
    """Business""": """Negócios""",
    """BUSINESS""": """NEGÓCIOS""",
    """Tips""": """Dicas""",
    """TIPS""": """DICAS""",
    """August 25, 2023""": """25 de Agosto de 2023""",
    """April 8, 2022""": """8 de Abril de 2022""",
    """August 18, 2023""": """18 de Agosto de 2023""",
    """The Ultimate Beard Grooming Kit for the Modern Gentleman""": """O Kit Definitivo de Cuidados com a Barba para o Cavalheiro Moderno""",
    """THE ULTIMATE BEARD GROOMING KIT FOR THE MODERN GENTLEMAN""": """O KIT DEFINITIVO DE CUIDADOS COM A BARBA PARA O CAVALHEIRO MODERNO""",
    """Unlocking the Art of Timeless Grooming: A Journey to the Barber Shop""": """Desvendando a Arte dos Cuidados Atemporais: Uma Jornada à Barbearia""",
    """UNLOCKING THE ART OF TIMELESS GROOMING: A JOURNEY TO THE BARBER SHOP""": """DESVENDANDO A ARTE DOS CUIDADOS ATEMPORAIS: UMA JORNADA À BARBEARIA""",
    """Mastering the Art of Beard Grooming: Tips and Techniques""": """Dominando a Arte de Cuidar da Barba: Dicas e Técnicas""",
    """MASTERING THE ART OF BEARD GROOMING: TIPS AND TECHNIQUES""": """DOMINANDO A ARTE DE CUIDAR DA BARBA: DICAS E TÉCNICAS""",
    """Browse All Articles""": """Ver Todos os Artigos""",
    """BROWSE ALL ARTICLES""": """VER TODOS OS ARTIGOS""",
    
    """Trimhub""": """Blade Barbearia""",
    """TrimHub""": """Blade Barbearia""",
    """TRIMHUB""": """BLADE BARBEARIA""",
    """Home""": """Início""",
    """About Us""": """Sobre Nós""",
    """Pricing""": """Preços""",
    """Services""": """Serviços""",
    """Gallery""": """Galeria""",
    """Blog""": """Blog""",
    """Contact us""": """Fale Conosco""",
}

sorted_translations = dict(sorted(translations.items(), key=lambda item: len(item[0]), reverse=True))

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return

    original_content = content
    for eng, pt in sorted_translations.items():
        content = content.replace(eng, pt)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def main():
    dirs_to_check = ['public', 'dist', 'src', '.']
    for d in dirs_to_check:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            if 'node_modules' in root or '.git' in root:
                continue
            for file in files:
                if file.endswith('.mjs') or file.endswith('.js') or file.endswith('.html'):
                    process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
