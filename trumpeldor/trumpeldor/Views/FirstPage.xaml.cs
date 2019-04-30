using Plugin.Multilingual;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

using Plugin.Permissions;
using Plugin.Permissions.Abstractions;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class FirstPage : ContentPage
    {
        private GameController gc;
        public FirstPage()
        {
            InitializeComponent();
            israelButton.Source = ServerConection.URL_MEDIA + "israel.png";
            englandButton.Source = ServerConection.URL_MEDIA + "united-kingdom.png";
            info.Source = ServerConection.URL_MEDIA + "information.png";
            how.Source = ServerConection.URL_MEDIA + "how.png";
            CrossMultilingual.Current.CurrentCultureInfo = new CultureInfo("he");
            gc = GameController.getInstance();
        }

        private async Task<bool> CanUserPlay()
        {
            if (!gc.IsUserInValidSector()){
                errorMessage.Text = AppResources.Out_Of_Valid_Sector_Title + "\n" + AppResources.Out_Of_Valid_Sector_Message;
                if (ServerConection.DEBUG == 1)
                    return await DisplayAlert("Debug Mode", "Do you want to continue", "yes", "no");
                return false;
            }
            return true;
        }

        private Task<bool> AskPermissionToUseLocation()
        {
            var task = Task.Run(async () =>{
                Permission permission = Permission.Location;
                var permissionStatus = await CrossPermissions.Current.CheckPermissionStatusAsync(permission);
                if (permissionStatus != PermissionStatus.Granted){
                    var response = await CrossPermissions.Current.RequestPermissionsAsync(permission);
                    return response[permission] == PermissionStatus.Granted;
                }
                return true;
            });
            return task;
        }

        private async void Play_Button_Clicked(object sender, EventArgs e)
        {
            while (!await AskPermissionToUseLocation()) ;
            if(await CanUserPlay())
                await Navigation.PushModalAsync(new LoginsPage());
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new instructionsPage());
        }

        private async void Info_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage());
        }

        private void English_Button_Clicked(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = new CultureInfo("en");
            DeleteBordersToCountries();
            englandButton.BorderWidth = 1;
            englandButton.BorderColor = Color.Black;
        }

        private void Hebrew_Button_Clicked(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = new CultureInfo("he");
            DeleteBordersToCountries();
            israelButton.BorderWidth = 1;
            israelButton.BorderColor = Color.Black;
        }

        private void DeleteBordersToCountries()
        {
            foreach (View child in countriesStackLayout.Children){
                ((ImageButton)child).BorderColor = countriesStackLayout.BackgroundColor;
                ((ImageButton)child).BorderWidth = 0;
            }
        }
    }
}