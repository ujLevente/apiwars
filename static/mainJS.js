function checkingPasswordSimilarity() {
    let registerBtn = document.getElementById('register-btn')
    registerBtn.addEventListener('click', function () {
        let passwordAgain = registerBtn.previousElementSibling;
        let password = passwordAgain.previousElementSibling;
        if (passwordAgain.value != password.value) {
            alert('passwords are not matching!')
        }
    })
}



function main() {
    checkingPasswordSimilarity();
}


main();