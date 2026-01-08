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
        mail : {
            personal: "personal@gmail.com",
            work: "work@gmail.com"
        }
    }
}

 for (let i in patientdetails) {
    if (typeof patientdetails[i] === 'object') {
        for (let j in patientdetails[i]) {
            if (typeof patientdetails[i][j] === 'object') {
                for (let k in patientdetails[i][j]) {
                    console.log(i, j, k, ":", patientdetails[i][j][k]);
                }
            } else {
                console.log(i, j, ":", patientdetails[i][j]);
            }
        }
    } else {
        console.log(i, ":", patientdetails[i]);
    }  
}     