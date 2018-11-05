using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class firsPagexaml : ContentPage
	{
		public firsPagexaml ()
		{
			InitializeComponent ();
		}

        private void Play_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new groupCreationPage();
        }

        private void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new instructionsPage();
        }

        private void Info_Button_Clicked(object sender, EventArgs e)
        {
            /*
                * with back click 
                * async
                * await Navigation.PushModalAsync(new NavigationPage(new informationPage()));
            */
            Application.Current.MainPage = new informationPage();
        }

        
    }
}