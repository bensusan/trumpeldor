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
        public const string ClientId = "416426124345-igghe7dik01k4e6jrgtmikpevjm3auvm.apps.googleusercontent.com";
        public const string Scope = "email";
        public const string RedirectUrl = "com.companyname.trumpeldor:/oauth2redirect";
    }
}