document.getElementById('validacion').addEventListener('submit', function(evento){
    evento.preventDefault();

    let nombre = document.getElementById('nombre').value;
    let usuario = document.getElementById('usuario').value;
    let documento = document.getElementById('documento').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    if (nombre === '') {
    alert('Escribi tu nombre completo');
    return false;
    }

    if (usuario === '') {
        alert('Escribi tu usuario');
        return false;
        }

    if (email === '') {
        alert('Escribi tu correo electrónico');
        return false;
        }

    if (password === '') {
        alert('Escribi tu contraseña');
        return false;
        }

    this.submit();
});