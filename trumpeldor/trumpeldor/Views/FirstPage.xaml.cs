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
        private bool firstAppear;
		public FirstPage ()
		{
            InitializeComponent();
            gc = GameController.getInstance();
            firstAppear = true;
        }

        public FirstPage(bool firstAppear) : this()
        {
            this.firstAppear = firstAppear;
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            if (this.firstAppear)
            {
                AskPermissionToUseLocation();
                ShowMessagesInStart();
            }
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

        private void AskPermissionToUseLocation()
        {

            Task.Run(async () =>
            {
                Permission permission = Permission.Location;
                var permissionStatus = await CrossPermissions.Current.CheckPermissionStatusAsync(permission);
                while (permissionStatus != PermissionStatus.Granted)
                {
                    var response = await CrossPermissions.Current.RequestPermissionsAsync(permission);
                    permissionStatus = response[permission];
                }
            });
        }

        private void ShowMessagesInStart()
        {
            Task.Run(() =>
            {
                List<OpenMessage> messagesToShow = gc.GetOpenMessages();
                foreach (OpenMessage om in messagesToShow)
                {
                    Device.BeginInvokeOnMainThread(async () => {
                        await DisplayAlert(om.title, om.data, AppResources.ok);
                    });
                }
            });
        }

        private void Play_Button_Clicked(object sender, EventArgs e)
        {
            //Application.Current.MainPage = new groupCreationPage();
            Application.Current.MainPage = new LoginsPage();
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new instructionsPage());
        }

        private async void Info_Button_Clicked(object sender, EventArgs e)
        {
            /*
                * with back click 
                * async
                * await Navigation.PushModalAsync(new NavigationPage(new informationPage()));
            */
            await Navigation.PushModalAsync(new informationPage());
            //Application.Current.MainPage = new informationPage();
        }


    }
}