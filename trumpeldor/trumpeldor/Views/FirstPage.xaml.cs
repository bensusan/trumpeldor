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

        private void Play_Button_Clicked(object sender, EventArgs e)
        {
            //Application.Current.MainPage = new groupCreationPage();
            Application.Current.MainPage = new LoginsPage();
        }

        private void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            Application.Current.MainPage = new instructionsPage();



            //await Navigation.PushModalAsync(new MapPage());
            //Application.Current.MainPage = new NavigationPage();


            //Task<byte[]> ans = ((App)(Application.Current)).getGameController().getFile();
            //byte[] fileBytes = await ans;
            ////Image image = new Image();
            //Stream stream = new MemoryStream(fileBytes);


            //tryImg.IsVisible = true;
            //tryImg.Source = ImageSource.FromStream(() => new MemoryStream(fileBytes));


            //await Navigation.PushModalAsync(new instructionsPage());
        }

        private void Info_Button_Clicked(object sender, EventArgs e)
        {
            /*
                * with back click 
                * async
                * await Navigation.PushModalAsync(new NavigationPage(new informationPage()));
            */
            Application.Current.MainPage = new informationPage();

            //await Navigation.PushModalAsync(new HintPage("31.263440,34.799115"));
            //await Navigation.PushModalAsync(new HintPage("http://132.72.23.64:12345/media/x.jpg"));
            //await Navigation.PushModalAsync(new HintPage("this is a text hint"));
            //await Navigation.PushModalAsync(new MapPage(new Point(31.263440, 34.799115)));
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
    }
}