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
            facebook.Source = ServerConection.URL_MEDIA + "facebook.png";
            google.Source = ServerConection.URL_MEDIA + "google.png";
            _googleManager = DependencyService.Get<IGoogleManager>();
        }

        private async void FacebookLogin_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new AccessFacebookProfile());
        }

        private void GoogleLogin_Clicked(object sender, EventArgs e)
        {
            _googleManager.Login(OnLoginComplete);
        }

        private async void Anonymus_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new groupCreationPage());
        }



        /*******************************************************************************/
        //Google sign in
        /*******************************************************************************/

        private readonly IGoogleManager _googleManager;

        private void OnLoginComplete(GoogleUser googleUser, string message)
        {
            if (googleUser != null)
                Application.Current.MainPage = new groupCreationPage(googleUser.ID, User.SOCIAL_NETWORK.Google);
            else
                Device.BeginInvokeOnMainThread(async () =>{
                    await DisplayAlert(AppResources.error, AppResources.error_in_google_login, AppResources.ok);
                });
        }
    }
}