from core.models import User , Profile


def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze

def usuario_natan():
    nat = User.objects.create_user(
        username='Natan',
        first_name='Natan',
        last_name='Viana',
        email='natanvianat16@gmail.com',
        password='snow',
    )
    Profile.objects.create(usuario=nat , avatar='https://lh3.googleusercontent.com/-aCuJKjbIDuQ/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucnYEx3SR7ACRGWptCOniEdpAj7oPg/s96-c/photo.jpg'
                           , nome='Natan', email='natanvianat16@gmail.com')
    #deveria criar cliente também?

    return nat


