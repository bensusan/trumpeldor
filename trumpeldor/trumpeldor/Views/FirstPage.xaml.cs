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
        private CultureInfo hebrew = new CultureInfo("he");
        private CultureInfo english = new CultureInfo("en");

        public FirstPage()
        {
            InitializeComponent();
            israelButton.Source = ServerConnectionImpl.URL_MEDIA + "israel.png";
            englandButton.Source = ServerConnectionImpl.URL_MEDIA + "united-kingdom.png";
            info.Source = ServerConnectionImpl.URL_MEDIA + "information.png";
            how.Source = ServerConnectionImpl.URL_MEDIA + "how.png";
            CrossMultilingual.Current.CurrentCultureInfo = hebrew;
            gc = GameController.getInstance();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            DeleteBordersToCountries();
            if (CrossMultilingual.Current.CurrentCultureInfo.Equals(hebrew))
            {
                israelButton.BorderWidth = 1;
                israelButton.BorderColor = Color.Black;
            }
            else if (CrossMultilingual.Current.CurrentCultureInfo.Equals(english))
            {
                englandButton.BorderWidth = 1;
                englandButton.BorderColor = Color.Black;
            }

        }

        private async Task<bool> CanUserPlay()
        {
            if (!gc.IsUserInValidSector()){
                errorMessage.Text = AppResources.Out_Of_Valid_Sector_Title + "\n" + AppResources.Out_Of_Valid_Sector_Message;
                if (ServerConnectionImpl.DEBUG == 1)
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
            gc.StartTaskLocation();
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
            CrossMultilingual.Current.CurrentCultureInfo = english;
            DeleteBordersToCountries();
            englandButton.BorderWidth = 1;
            englandButton.BorderColor = Color.Black;
            if(errorMessage.Text != "")
                errorMessage.Text = AppResources.Out_Of_Valid_Sector_Title + "\n" + AppResources.Out_Of_Valid_Sector_Message;
        }

        private void Hebrew_Button_Clicked(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = hebrew;
            DeleteBordersToCountries();
            israelButton.BorderWidth = 1;
            israelButton.BorderColor = Color.Black;
            if (errorMessage.Text != "")
                errorMessage.Text = AppResources.Out_Of_Valid_Sector_Title + "\n" + AppResources.Out_Of_Valid_Sector_Message;
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