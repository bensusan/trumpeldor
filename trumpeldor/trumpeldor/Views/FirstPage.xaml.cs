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
		public FirstPage ()
		{
            InitializeComponent();
            gc = GameController.getInstance();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            ShowRelevantFunctionalitiesAccordingToLocation();
    }

        private void ShowRelevantFunctionalitiesAccordingToLocation()
        {
            Task.Run(() =>
            { 
                if (!gc.IsUserInValidSector())
                {
                    Device.BeginInvokeOnMainThread(async () => {
                        await DisplayAlert(AppResources.Out_Of_Valid_Sector_Title, AppResources.Out_Of_Valid_Sector_Message, AppResources.ok);
                    });
                    if (ServerConection.DEBUG == 1)
                        Device.BeginInvokeOnMainThread(async() => {
                            await DisplayAlert("Debug Mode", "This functionality does not work in debug mode", "ok");
                        });
                    else
                        playButton.IsVisible = false;
                }
            });
        }

        private Task<bool> AskPermissionToUseLocation()
        {

            //Task.Run(async () =>
            //{
            //    Permission permission = Permission.Location;
            //    var permissionStatus = await CrossPermissions.Current.CheckPermissionStatusAsync(permission);
            //    while (permissionStatus != PermissionStatus.Granted)
            //    {
            //        var response = await CrossPermissions.Current.RequestPermissionsAsync(permission);
            //        permissionStatus = response[permission];
            //    }
            //});

            var task = Task.Run(async () =>
            {
                Permission permission = Permission.Location;
                var permissionStatus = await CrossPermissions.Current.CheckPermissionStatusAsync(permission);
                if (permissionStatus != PermissionStatus.Granted)
                {
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
    }
}