﻿using System;

using Android.App;
using Android.Content.PM;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;
using trumpeldor.Configuration;
using trumpeldor.Droid.Configuration;

using trumpeldor.Services;
using Android.Gms.Auth.Api.SignIn;
using Android.Gms.Auth.Api;
using Xamarin.Forms;
using trumpeldor.Services.Contracts;

namespace trumpeldor.Droid
{
    [Activity(Label = "trumpeldor", Icon = "@mipmap/icon", Theme = "@style/MainTheme", MainLauncher = true, ConfigurationChanges = ConfigChanges.ScreenSize | ConfigChanges.Orientation)]
    public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsAppCompatActivity
        //, IGoogleAuthenticationDelegate
    {
        //public static GoogleAuthenticator Auth;


        protected override void OnCreate(Bundle savedInstanceState)
        {
            TabLayoutResource = Resource.Layout.Tabbar;
            ToolbarResource = Resource.Layout.Toolbar;

            base.OnCreate(savedInstanceState);

            DependencyService.Register<IGoogleManager, GoogleManager>();

            global::Xamarin.Forms.Forms.Init(this, savedInstanceState);
            ConfigurationManager.Initialize(new AndroidConfigurationStreamProviderFactory(() => this));
            Xamarin.FormsMaps.Init(this, savedInstanceState);//for maps init
            LoadApplication(new App());
        }

        public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Android.Content.PM.Permission[] grantResults)
        {
            Plugin.Permissions.PermissionsImplementation.Current.OnRequestPermissionsResult(requestCode, permissions, grantResults);
            base.OnRequestPermissionsResult(requestCode, permissions, grantResults);
        }

        protected override void OnActivityResult(int requestCode, Result resultCode, Android.Content.Intent data)
        {
            base.OnActivityResult(requestCode, resultCode, data);
            if (requestCode == 1)
            {
                GoogleSignInResult result = Auth.GoogleSignInApi.GetSignInResultFromIntent(data);
                GoogleManager.Instance.OnAuthCompleted(result);
            }
        }
    }
}