let patientdetails = {
    name : "Shweta",
    place : "Bengaluru",
    disease : "Heart Broken",
    DOA : "01/01/2026",
    weight : "35kg",
    height : `5'10"`,
    bloodgroup : "B+ve",
    contact : {
        mobile : 9843294384,
        mail : "Shweta1@gamil.com"
    }
}

for (let i in patientdetails) {
    if (typeof patientdetails[i] === 'object') {
        for (let j in patientdetails[i]) {
            console.log(j.patientdetails[i][j])
        }
    }else{
        console.log(i, ":", patientdetails[i])
    }
        
}