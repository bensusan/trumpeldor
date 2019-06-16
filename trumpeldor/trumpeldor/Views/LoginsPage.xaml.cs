using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.Models;
using trumpeldor.Services.Contracts;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class LoginsPage : ContentPage
	{
		public LoginsPage ()
		{
			InitializeComponent ();
            //facebook.Source = ServerConection.URL_MEDIA + "facebook.png";
            //google.Source = ServerConection.URL_MEDIA + "google.png";
            _googleManager = DependencyService.Get<IGoogleManager>();
        }

        private async void FacebookLogin_Clicked(object sender, EventArgs e)
        {
            ButtonsLocker.LockAll(btnLayout);
            await Navigation.PushModalAsync(new AccessFacebookProfile());
            ButtonsLocker.UnlockAll(btnLayout);
        }

        private void GoogleLogin_Clicked(object sender, EventArgs e)
        {
            ButtonsLocker.LockAll(btnLayout);
            _googleManager.Login(OnLoginComplete);
            ButtonsLocker.UnlockAll(btnLayout);
        }

        private async void Anonymus_Clicked(object sender, EventArgs e)
        {
            ButtonsLocker.LockAll(btnLayout);
            if (await DisplayAlert(AppResources.login_as_anonymous, AppResources.anonymous_alert, AppResources.Yes, AppResources.No))
                await Navigation.PushModalAsync(new groupCreationPage());
            ButtonsLocker.UnlockAll(btnLayout);
        }



        /*******************************************************************************/
        //Google sign in
        /*******************************************************************************/

        private readonly IGoogleManager _googleManager;

        private void OnLoginComplete(GoogleUser googleUser, string message)
        {
            if (googleUser != null)
            {
                //TODO
                //if(GameController.getInstance().IsAdmin(googleUser.Email));
                //Application.Current.MainPage = new AdminPage(googleUser);
                ContentPage nextPage = new groupCreationPage(googleUser.ID, User.SOCIAL_NETWORK.Google);
                _googleManager.Logout();
                Application.Current.MainPage = nextPage;
            }
            else
                Device.BeginInvokeOnMainThread(async () =>
                {
                    await DisplayAlert(AppResources.error, AppResources.error_in_google_login, AppResources.ok);
                });
        }
    }
}