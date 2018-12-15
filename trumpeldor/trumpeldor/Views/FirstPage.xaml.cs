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
    public partial class FirstPage : ContentPage
    {
		public FirstPage ()
		{
			InitializeComponent();
		}

        private async void Play_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new groupCreationPage());
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new instructionsPage());
        }

        private async void Info_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage());
            
            //without back click
            //Application.Current.MainPage = new informationPage();
        }

        
    }
}