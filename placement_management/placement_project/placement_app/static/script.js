function validateForm(){

    let studentId =
    document.forms[0]["student_id"].value;

    let name =
    document.forms[0]["name"].value;

    let email =
    document.forms[0]["email"].value;

    let password =
    document.forms[0]["password"].value;

    let branch =
    document.forms[0]["branch"].value;

    let cgpa =
    document.forms[0]["cgpa"].value;

    if(studentId=="" ||
       name=="" ||
       email=="" ||
       password=="" ||
       branch=="" ||
       cgpa==""){

        alert("All fields are required");

        return false;
    }

    if(cgpa<0 || cgpa>10){

        alert("CGPA must be between 0 and 10");

        return false;
    }

    return true;
}


function togglePassword(id, element){

    let password =
    document.getElementById(id);

    let icon =
    element.querySelector("i");

    if(password.type==="password"){

        password.type="text";

        icon.classList.remove("fa-eye-slash");

        icon.classList.add("fa-eye");
    }

    else{

        password.type="password";

        icon.classList.remove("fa-eye");

        icon.classList.add("fa-eye-slash");
    }
}