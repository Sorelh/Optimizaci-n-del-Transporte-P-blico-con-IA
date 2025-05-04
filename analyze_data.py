import spacy

nlp = spacy.load('es_core_news_sm')

def analyze_data(data):
    for text in data:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ == 'LOC':
                if ent.text not in issues:
                    issues[ent.text] = 0
                    issues[ent.text] += 1   
                    print(f"analyze_data: {issues}")
                    return issues
    
            
if __name__ == "__main__":
    data = ['Historia de Colombia\n@colombia_hist\n·\n6h\nBogotá y el eterno problema de transporte público... Esta vez en 1985 #HistoriaDeColombia\n4\n25\n136\n3 mil', 'Pedro Antonio Ocampo osorio\n@Pedroelgrande74\n·\n19min\nY que querían ? Bogota sin agua y en racionamiento, inundada por todos lados, el adefesio de metro que están haciendo que en vez de valorizar los predios por donde pasa los va es a destruir por el ruido y la contaminación  todo por el Bisnes de \n@EnriquePenalosa\n y \n@ClaudiaLopez\n1\n5\n50', 'Maria Fernanda\n@Mafecor11\n·\n2h\nQué horrible tomar transporte público en Bogotá jajaja  después de andar en moto por el pueblo.\n35', 'Historia de Colombia\n@colombia_hist\n·\n21 abr.\nEl eterno problema de transporte público de Bogotá, así era en la década de 1980. \n\n#ViajeEnElTiempo\n5\n72\n276\n6 mil', 'Jorge Emilio Rey Ángel\n@JorgeEmilioRey\n·\n31 mar.\nSe reporta un nuevo accidente en la vía #Bogotá—#Tunja, a la altura del municipio de #Gachancipá, en el sector El Roble. En esta ocasión, dos buses de transporte público, aparentemente por exceso de velocidad, provocaron el siniestro vial, que hasta el momento deja un saldo de 12\nMostrar más\n13\n17\n40\n20 mil', 'Anaa_\n@anansiosa_\n·\n29 abr.\nTe odio sistema de transporte público de Bogotá\n1\n4\n59', 'El Colombiano\n@elcolombiano\n·\n31 mar.\nDos buses chocaron en la vía Bogotá - Tunja, a la altura del municipio de Gachancipá, en Cundinamarca. \n\nEl choque se registró luego de que un bus de transporte público adscrito a la empresa Cootranzipa se detuviera para recoger a un usuario en un paradero. Sin embargo, en escena\nMostrar más\n55\n48\n133\n164 mil']
    issues = analyze_data(data)
    print(issues)