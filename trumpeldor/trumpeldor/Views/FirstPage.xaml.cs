﻿using Plugin.Multilingual;
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
using Rg.Plugins.Popup.Services;
using System.Diagnostics;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class FirstPage : ContentPage
    {
        private GameController gc;
        //private CultureInfo hebrew = new CultureInfo("he");
        //private CultureInfo english = new CultureInfo("en");

        public FirstPage()
        {
            InitializeComponent();
            israelButton.Source = ServerConection.URL_MEDIA + "israel.png";
            englandButton.Source = ServerConection.URL_MEDIA + "united-kingdom.png";
            //info.Source = ServerConection.URL_MEDIA + "information.png";
            //how.Source = ServerConection.URL_MEDIA + "how.png";
            gc = GameController.getInstance();
            CrossMultilingual.Current.CurrentCultureInfo = gc.hebrew;
            countriesStackLayout.FlowDirection = FlowDirection.RightToLeft;
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            DeleteBordersToCountries();
            if (CrossMultilingual.Current.CurrentCultureInfo.Equals(gc.hebrew))
            {
                israelButton.BorderWidth = 1;
                israelButton.BorderColor = Color.Black;
            }
            else if (CrossMultilingual.Current.CurrentCultureInfo.Equals(gc.english))
            {
                englandButton.BorderWidth = 1;
                englandButton.BorderColor = Color.Black;
            }

        }

        private async Task<bool> CanUserPlay()
        {
            if (!gc.IsUserInValidSector()){
                if (Debugger.IsAttached /*|| ServerConection.DEBUG == 1*/)
                {
                    return await DisplayAlert("Debug Mode", "Do you want to continue", "yes", "no");
                }
                else
                {
                    return false;
                }
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
            ButtonsLocker.LockAll(BtnLayout);
            while (!await AskPermissionToUseLocation()) ;
            gc.StartTaskLocation();
            if (await CanUserPlay())
                await Navigation.PushModalAsync(new LoginsPage());
            else
                await DisplayAlert("BGU ARTS", AppResources.Out_Of_Valid_Sector_Message, AppResources.ok);
            ButtonsLocker.UnlockAll(BtnLayout);
        }

        private async void HowToPlay_Button_Clicked(object sender, EventArgs e)
        {
            ButtonsLocker.LockAll(BtnLayout);
            await Navigation.PushModalAsync(new instructionsPage());
            ButtonsLocker.UnlockAll(BtnLayout);
        }

        private async void Info_Button_Clicked(object sender, EventArgs e)
        {
            ButtonsLocker.LockAll(BtnLayout);
            await Navigation.PushModalAsync(new informationPage());
            ButtonsLocker.UnlockAll(BtnLayout);
        }

        private void English_Button_Clicked(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = gc.english;
            DeleteBordersToCountries();
            englandButton.BorderWidth = 1;
            englandButton.BorderColor = Color.Black;
            updateLangInThisPage();
            //if(errorMessage.Text != "")
            //    errorMessage.Text = AppResources.Out_Of_Valid_Sector_Title + "\n" + AppResources.Out_Of_Valid_Sector_Message;
        }

        private void Hebrew_Button_Clicked(object sender, EventArgs e)
        {
            CrossMultilingual.Current.CurrentCultureInfo = gc.hebrew;
            DeleteBordersToCountries();
            israelButton.BorderWidth = 1;
            israelButton.BorderColor = Color.Black;
            updateLangInThisPage();
            //if (errorMessage.Text != "")
            //    errorMessage.Text = AppResources.Out_Of_Valid_Sector_Title + "\n" + AppResources.Out_Of_Valid_Sector_Message;
        }

        private void updateLangInThisPage()
        {
            how.Text = AppResources.how_to_play;
            playButton.Text = AppResources.play;
            info.Text = AppResources.informationFirstPage;
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