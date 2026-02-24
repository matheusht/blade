import os

translations = {
    '"ABOUT US"': '"SOBRE NÓS"',
    '`ABOUT US`': '`SOBRE NÓS`',
    '>ABOUT US<': '>SOBRE NÓS<',
    '"Haircuts"': '"Cortes"',
    '`Haircuts`': '`Cortes`',
    '>Haircuts<': '>Cortes<',
    '"Beard Grooming"': '"Cuidados com a Barba"',
    '`Beard Grooming`': '`Cuidados com a Barba`',
    '>Beard Grooming<': '>Cuidados com a Barba<',
    '"Facials"': '"Limpeza de Pele"',
    '`Facials`': '`Limpeza de Pele`',
    '>Facials<': '>Limpeza de Pele<',
    '"Styling"': '"Penteados"',
    '`Styling`': '`Penteados`',
    '>Styling<': '>Penteados<',
    '"Home"': '"Início"',
    '`Home`': '`Início`',
    '>Home<': '>Início<',
    '"About Us"': '"Sobre Nós"',
    '`About Us`': '`Sobre Nós`',
    '>About Us<': '>Sobre Nós<',
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
    '"Hair Color"': '"Coloração"',
    '`Hair Color`': '`Coloração`',
    '>Hair Color<': '>Coloração<',
    'TrimHub': 'Blade Barbearia',
    'Trimhub': 'Blade Barbearia',
    'TRIMHUB': 'BLADE BARBEARIA',
    """Welcome to TrimHub, where grooming is an art, precision is our creed, and your style is our canvas. We're not just a barber shop; we're your trusted grooming partner on a journey of self-expression and confidence.""": """Bem-vindo à Blade Barbearia, onde o cuidado é uma arte, a precisão é o nosso credo e o seu estilo é a nossa tela. Não somos apenas uma barbearia; somos o seu parceiro de confiança numa jornada de autoexpressão e confiança.""",
    """Welcome to TrimHub, where grooming is an art, precision is our creed, and your style is our canvas. We\\'re not just a barber shop; we\\'re your trusted grooming partner on a journey of self-expression and confidence.""": """Bem-vindo à Blade Barbearia, onde o cuidado é uma arte, a precisão é o nosso credo e o seu estilo é a nossa tela. Não somos apenas uma barbearia; somos o seu parceiro de confiança numa jornada de autoexpressão e confiança.""",
    """OUR LEGACY OF EXCELLENCE:""": """NOSSO LEGADO DE EXCELÊNCIA:""",
    """With years of experience in the industry, TrimHub stands as a beacon of grooming excellence. Our barbers are more than just professionals; they are artisans, meticulously crafting each haircut and beard trim to perfection. We take pride in our legacy of precision and the trust our clients place in us.""": """Com anos de experiência na indústria, a Blade Barbearia destaca-se como um farol de excelência em cuidados masculinos. Nossos barbeiros são mais do que profissionais; são artesãos, esculpindo meticulosamente cada corte de cabelo e barba com perfeição. Temos orgulho em nosso legado de precisão e na confiança que nossos clientes depositam em nós.""",
    """A SPACE OF DISTINCTION:""": """UM ESPAÇO DE DISTINÇÃO:""",
    """TrimHub is more than a grooming destination; it's an environment designed for your comfort and relaxation. Our modern and welcoming space is an oasis amidst the rush of everyday life. Here, you can unwind, unplug, and immerse yourself in the art of grooming.""": """A Blade Barbearia é mais do que um destino de cuidados masculinos; é um ambiente projetado para o seu conforto e relaxamento. Nosso espaço moderno e acolhedor é um oásis no meio da agitação do dia a dia. Aqui, você pode relaxar, desconectar e mergulhar na arte do cuidado.""",
    """TrimHub is more than a grooming destination; it\\'s an environment designed for your comfort and relaxation. Our modern and welcoming space is an oasis amidst the rush of everyday life. Here, you can unwind, unplug, and immerse yourself in the art of grooming.""": """A Blade Barbearia é mais do que um destino de cuidados masculinos; é um ambiente projetado para o seu conforto e relaxamento. Nosso espaço moderno e acolhedor é um oásis no meio da agitação do dia a dia. Aqui, você pode relaxar, desconectar e mergulhar na arte do cuidado.""",
    """We invite you to experience TrimHub – a place where tradition meets innovation, where precision meets artistry, and where grooming becomes an extraordinary experience. Whether you're seeking a classic cut, a rejuvenating shave, or a stylish transformation, our doors are open to welcome you into the world of timeless grooming and experience:""": """Convidamos você a experimentar a Blade Barbearia – um lugar onde a tradição encontra a inovação, onde a precisão encontra a arte, e onde o cuidado se torna uma experiência extraordinária. Se você busca um corte clássico, um barbear rejuvenescedor ou uma transformação estilosa, nossas portas estão abertas para recebê-lo no mundo dos cuidados e experiências atemporais:""",
    """We invite you to experience TrimHub – a place where tradition meets innovation, where precision meets artistry, and where grooming becomes an extraordinary experience. Whether you\\'re seeking a classic cut, a rejuvenating shave, or a stylish transformation, our doors are open to welcome you into the world of timeless grooming and experience:""": """Convidamos você a experimentar a Blade Barbearia – um lugar onde a tradição encontra a inovação, onde a precisão encontra a arte, e onde o cuidado se torna uma experiência extraordinária. Se você busca um corte clássico, um barbear rejuvenescedor ou uma transformação estilosa, nossas portas estão abertas para recebê-lo no mundo dos cuidados e experiências atemporais:""",
    """Personalized Styling""": """Estilo Personalizado""",
    """Client-Centric Approach""": """Abordagem Centrada no Cliente""",
    """Luxurious Shaves""": """Barbear Luxuoso""",
    """Your journey with us is personal. We understand that every client is unique, and that's why our services are tailored to suit your preferences and lifestyle. Whether you're looking for a classic haircut, a rejuvenating facial treatment, or the perfect beard trim, we've got you covered.""": """Sua jornada conosco é pessoal. Entendemos que cada cliente é único, e é por isso que nossos serviços são feitos sob medida para atender às suas preferências e estilo de vida. Seja para um corte de cabelo clássico, um tratamento facial rejuvenescedor ou o aparo perfeito da barba, nós temos o que você precisa.""",
    """Your journey with us is personal. We understand that every client is unique, and that\\'s why our services are tailored to suit your preferences and lifestyle. Whether you\\'re looking for a classic haircut, a rejuvenating facial treatment, or the perfect beard trim, we\\'ve got you covered.""": """Sua jornada conosco é pessoal. Entendemos que cada cliente é único, e é por isso que nossos serviços são feitos sob medida para atender às suas preferências e estilo de vida. Seja para um corte de cabelo clássico, um tratamento facial rejuvenescedor ou o aparo perfeito da barba, nós temos o que você precisa.""",
    """Beyond the grooming chair, we believe in building connections. TrimHub is a place where conversations flow as smoothly as the clippers. It's a hub where stories are shared, experiences are cherished, and camaraderie is formed. Our clients are more than just customers; they're part of our community. Our stats say the words:""": """Além da cadeira de barbeiro, acreditamos em construir conexões. A Blade Barbearia é um lugar onde as conversas fluem tão suavemente quanto as máquinas de cortar. É um ponto de encontro onde histórias são compartilhadas, experiências são valorizadas e a camaradagem é formada. Nossos clientes são mais do que clientes; eles fazem parte da nossa comunidade. Nossos números dizem por si:""",
    """Beyond the grooming chair, we believe in building connections. TrimHub is a place where conversations flow as smoothly as the clippers. It\\'s a hub where stories are shared, experiences are cherished, and camaraderie is formed. Our clients are more than just customers; they\\'re part of our community. Our stats say the words:""": """Além da cadeira de barbeiro, acreditamos em construir conexões. A Blade Barbearia é um lugar onde as conversas fluem tão suavemente quanto as máquinas de cortar. É um ponto de encontro onde histórias são compartilhadas, experiências são valorizadas e a camaradagem é formada. Nossos clientes são mais do que clientes; eles fazem parte da nossa comunidade. Nossos números dizem por si:""",
    """-FOUNDER, TRIMHUB BARBERSHOP""": """-FUNDADOR, BLADE BARBEARIA""",
    """OUR TEAM""": """NOSSA EQUIPE""",
    """MEET OUR EXPERT BARBERS""": """CONHEÇA NOSSOS BARBEIROS ESPECIALISTAS""",
    """Our team of expert barbers brings together passion, skill, and dedication to elevate your grooming experience.""": """Nossa equipe de barbeiros especialistas reúne paixão, habilidade e dedicação para elevar sua experiência de cuidado pessoal.""",
    """Hair Specialist""": """Especialista em Cabelo""",
    """Beard Grooming Expert""": """Especialista em Barba""",
    """Facial Treatments Specialist""": """Especialista em Tratamentos Faciais""",
    """Color Specialist""": """Especialista em Coloração""",
    '"GET IN TOUCH"': '"ENTRE EM CONTATO"',
    '`GET IN TOUCH`': '`ENTRE EM CONTATO`',
    '>GET IN TOUCH<': '>ENTRE EM CONTATO<',
    """Feel free to reach out to us with your inquiries through either phone or email. We are here to provide you with the information you need.""": """Sinta-se à vontade para entrar em contato com suas dúvidas, seja por telefone ou e-mail. Estamos aqui para fornecer as informações que você precisa.""",
    '"SEND US A MESSAGE"': '"ENVIE-NOS UMA MENSAGEM"',
    '`SEND US A MESSAGE`': '`ENVIE-NOS UMA MENSAGEM`',
    '>SEND US A MESSAGE<': '>ENVIE-NOS UMA MENSAGEM<',
    '"NAME"': '"NOME"',
    '`NAME`': '`NOME`',
    '>NAME<': '>NOME<',
    '"PHONE"': '"TELEFONE"',
    '`PHONE`': '`TELEFONE`',
    '>PHONE<': '>TELEFONE<',
    '"EMAIL"': '"E-MAIL"',
    '`EMAIL`': '`E-MAIL`',
    '>EMAIL<': '>E-MAIL<',
    '"MESSAGE"': '"MENSAGEM"',
    '`MESSAGE`': '`MENSAGEM`',
    '>MESSAGE<': '>MENSAGEM<',
    """Write your Message""": """Escreva sua mensagem""",
    '"SUBMIT"': '"ENVIAR"',
    '`SUBMIT`': '`ENVIAR`',
    '>SUBMIT<': '>ENVIAR<',
    '"CONTACT INFORMATION"': '"INFORMAÇÕES DE CONTATO"',
    '`CONTACT INFORMATION`': '`INFORMAÇÕES DE CONTATO`',
    '>CONTACT INFORMATION<': '>INFORMAÇÕES DE CONTATO<',
    """Opening Hours:""": """Horário de Funcionamento:""",
    """Elevating Grooming. Inspiring Style. Unleash Your Confidence at TrimHub where we craft exceptional looks that reflect your individuality a passion for style and an eye for detail.""": """Elevando o Cuidado. Inspirando o Estilo. Libere sua confiança na Blade Barbearia, onde criamos looks excepcionais que refletem sua individualidade, uma paixão por estilo e atenção aos detalhes.""",
    """QUICK LINKS""": """LINKS RÁPIDOS""",
    """Quick Links""": """Links Rápidos""",
    '"LEGAL"': '"LEGAL"',
    '`LEGAL`': '`LEGAL`',
    '>LEGAL<': '>LEGAL<',
    """Privacy Policy""": """Política de Privacidade""",
    '"Privacy policy"': '"Política de Privacidade"',
    '`Privacy policy`': '`Política de Privacidade`',
    '>Privacy policy<': '>Política de Privacidade<',
    '"Terms & Conditions"': '"Termos e Condições"',
    '`Terms & Conditions`': '`Termos e Condições`',
    '>Terms & Conditions<': '>Termos e Condições<',
    """Terms &amp; Conditions""": """Termos e Condições""",
    """FOLLOW US ON""": """SIGA-NOS NO""",
    """Follow us on""": """Siga-nos no""",
    """©TEMPLATE BY REALMEHEDI""": """©TEMPLATE POR REALMEHEDI""",
    """©Template by RealMehedi""": """©Template por RealMehedi""",
    """BUILT IN FRAMER""": """FEITO NO FRAMER""",
    """Built in Framer""": """Feito no Framer""",
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
