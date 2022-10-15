window.addEventListener('load', function() {
    let params = getParameters();

    if (params['id_token'] !== undefined) {
        if (getCookie('logged_in' !== 'true')) {
            document.cookie = "logged_in=true";
            document.cookie = "id_token=" + params['id_token'];
        }
        $('.login').find('.navBarLink').html('Logout');
    } else {
        loginButton();
    }
});

function loginButton () {
    let button = $('.login').find('.navBarLink');
    button.html('Login');
    button.attr('href', 'https://auth.vseth.ethz.ch/auth/realms/VSETH/protocol/openid-connect/auth?client_id=vseth-team-11&response_type=id_token&redirect_url=localhost&nonce=' + randstring(12));
}

function randstring(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() *
            charactersLength));
    }
    return result;
}

function getParameters()
{
    let url = window.location.search.substring(1);
    let params = url.split('&');

    let parameters = {};
    for (let i = 0; i < params.length; i++) {
        let split = params[i].split('=');
        parameters[split[0]] = split[1];
    }

    return parameters;
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}