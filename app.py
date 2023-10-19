from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#Find mode emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="CV data anlayst", page_icon=":tada", layout="wide")

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/51d5730b-905f-4822-83fd-b9bf52e0e500/fzaw4emYp0.json")
img_contact = Image.open("images/project.png")


with st.container():
	st.subheader("Bonjour moi c'est Jaures :wave:")
	st.title("Data analyst a la SOLIBRA, Côte D'ivoire")
	st.write("je suis passionné des nouvelles technologies et de tout ce qui touche au données.")
	st.write("En résume je suis 'Data Analyst' avec des aptitudes en Programmation. Je cherche à poursuivre une carrière où je peux utiliser mes compétences en SQL, Python, VBA, Tableau et PowerBI en développant de solides relations commerciales.")
	st.write("[Voir plus](https://www.linkedin.com/in/ndajaures/)")

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Mes competances")
		st.write("##")
		st.write(
			"""
			En tant qu'expert en data analysis, je maîtrise parfaitement des langages tels que Python, R et SQL, ainsi que des outils
			comme Pandas et Scikit-learn. J'applique des méthodes statistiques avancées et utilise l'apprentissage automatique pour
			résoudre des problèmes complexes. La manipulation de grandes quantités de données, y compris celles issues de systèmes Big 
			Data, fait partie de mes compétences. Je suis également très compétent dans le nettoyage et la préparation des données pour
			l'analyse. Ma capacité à communiquer clairement les résultats et à créer des visualisations informatives est cruciale pour
			influencer les décisions commerciales. Enfin, je suis très conscient des enjeux éthiques et de confidentialité liés à la
			manipulation des données.
			"""
			)
		st.write("[Voir plus](https://www.linkedin.com/in/ndajaures/)")

	with right_column:
		st_lottie(lottie_coding, height=300, key="coding")


with st.container():
	st.write("---")
	st.header("Mes projets")
	st.write("##")
	image_column, text_column = st.columns((1,2))
	with image_column:
		st.image(img_contact)
	with text_column:
		st.subheader("projet d'analyse de données visant à optimiser les campagnes marketing d'une entreprise")
		st.write(
			"""
			  Je vais élaborer un projet d'analyse de données visant à optimiser les campagnes marketing d'une entreprise. Je vais
			  collecter, nettoyer et analyser les données des clients pour identifier les segments les plus rentables. En utilisant
			  des techniques d'apprentissage automatique, je développerai un modèle de prédiction de comportement d'achat. Enfin, je
			  fournirai des recommandations pour améliorer le ciblage marketing et maximiser les conversions, en mettant l'accent sur
			  la confidentialité des données.
			"""
			)
		st.markdown("[Voir plus](https://www.linkedin.com/in/ndajaures/)")


with st.container():
	st.write("---")
	st.header("Me contactez")
	st.write("##")

	contact_form = """
		<form action="https://formsubmit.co/ndajeanjaures@gmail.com" method="POST">
			<input type="hidden" name="_captcha" value="false">
		    <input type="text" name="name" placeholder="Entrez votre nom" required>
		    <input type="email" name="email" placeholder="Entrez votre Email" required>
		    <textarea name="message" placeholder="Votre message ici" required></textarea>
		    <button type="submit">Envoyer</button>
		</form> 
	"""

	left_column, right_column = st.columns(2)
	with left_column:
		st.markdown(contact_form, unsafe_allow_html=True)
	with right_column:
		st.empty()
		
