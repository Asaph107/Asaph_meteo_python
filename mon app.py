from flask import Flask, render_template, request, redirect, url_for, redirect
from temperature import temps
app = Flask(__name__)





@app.route('/')
def bonjour():
    return render_template("index.html")



@app.route("/city", methods=["POST"])
def city():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    city = request.form
    localisation = city.get('city')
    valeurs = temps(localisation)

    # Monoxyde_de_carbones_app = valeurs[0] +""
    # Dioxyde_d_azotes_app = valeurs[1] +""
    # vitesse_du_vent_app = valeurs[2] +""
    # temperature_app = valeurs[3] +""
    # temperature_max_app = valeurs[4] +""
    # temperature_min_app = valeurs[5] +""
    # humidite_app = valeurs[6] +""
    


    
    print (type(valeurs))
    print(valeurs)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return render_template("traitement.html", emplacement = valeurs, ville = localisation)

    # return(Monoxyde_de_carbones,Dioxyde_d_azotes,vitesse_du_vent,temperature,temperature_max,temperature_min,humidite)


if __name__ == '__main__':
    app.run(debug=True)
