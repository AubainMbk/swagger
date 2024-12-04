nom = document.getElementById("nom");
prenom = document.getElementById("prenom");
bio = document.getElementById("bio");
exp_pro = document.getElementById("exp_pro");
competences = document.getElementById("competences");
cv = document.getElementById("cv");


btn_submit = document.getElementById("btn_submit");

btn_submit.addEventListener("click", function(){
    alert(nom.value)
    const data = {
        nom: nom.value,
        prenom: prenom.value,
        bio: bio.value,
        exp_pro: exp_pro.value,
        competences: competences.value,
        cv: cv.value
    };

    fetch('json_db.json', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});