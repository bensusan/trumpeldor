using System;
using System.Collections.Generic;
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
            //Application.Current.MainPage = new instructionsPage();



            //await Navigation.PushModalAsync(new MapPage());
            Application.Current.MainPage = new NavigationPage();


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
        }

        
    }
}