using Plugin.Multilingual;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
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
            await Navigation.PushModalAsync(new LoginsPage());
            //Application.Current.MainPage = new LoginsPage();
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new instructionsPage());
            //Application.Current.MainPage = new instructionsPage();
        }

        private async void Info_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage());
            //Application.Current.MainPage = new informationPage();
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = new CultureInfo("en");
            Application.Current.MainPage = new FirstPage();
        }

        private void Button_Clicked_1(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = new CultureInfo("he");
            Application.Current.MainPage = new FirstPage();
        }

        /*
        private void Shortcut_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new NavigationPage();
        }
        */
        
    }
}