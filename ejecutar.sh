# Este Script es llamado al inciarse el contenedor Docker

waitress-serve --listen=*:8080 --call 'lectorqr:create_app'
