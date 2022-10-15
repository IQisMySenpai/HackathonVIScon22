window.addEventListener('load', function() {
    let params = getParameters();

    if (params['id_token'] !== undefined) {
        document.cookie = 'id_token=' + params['id_token'] + '; path=/';
        history.pushState("", document.title, window.location.pathname);
    }
    let cookies = getCookies();
    if (cookies['id_token'] !== '' && cookies['id_token'] !== undefined) {
        let button = $('.login').find('.navBarLink');

        button.html('Logout');
        button.on('click', function() {
            button.off('click');
            document.cookie = 'id_token=; expires=Thu, 01 Jan 1970; path=/';
            window.setTimeout(loginButton, 100);
        });
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
    let url;
    if (window.location.hash !== '') {
        url = window.location.hash.substring(1);
    } else if (window.location.search !== '') {
        url = window.location.search.substring(1);
    } else {
        return {};
    }

    let params = url.split('&');

    let parameters = {};
    for (let i = 0; i < params.length; i++) {
        let split = params[i].split('=');
        parameters[split[0]] = split[1];
    }

    return parameters;
}

function getCookies() {
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    let cookies = {};
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        let split = c.split('=');
        cookies[split[0]] = split[1];
    }
    return cookies;
}

function version () {
    return '1.0.0';
}