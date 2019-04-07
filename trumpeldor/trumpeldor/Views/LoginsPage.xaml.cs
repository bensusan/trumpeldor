using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
		}

        private async void FacebookLogin_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new AccessFacebookProfile());
        }

        private async void GoogleLogin_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new AccessGoogleProfile());
        }

        private async void Anonymus_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new groupCreationPage());
        }
    }
}