using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace trumpeldor.Droid.Configuration
{
    public static class Configuration
    {
        public const string ClientId = "723962257721-ql0tki3si3s22l1lsovimivkmnrfm6rr.apps.googleusercontent.com";
        public const string Scope = "email";
        public const string RedirectUrl = "com.woodenmoose.xamarin.googleauth:/oauth2redirect";
    }
}