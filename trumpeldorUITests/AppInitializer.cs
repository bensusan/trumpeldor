using System;
using Xamarin.UITest;
using Xamarin.UITest.Queries;

namespace trumpeldorUITests
{
    public class AppInitializer
    {
        public static IApp StartApp(Platform platform)
        {
            if (platform == Platform.Android)
            {
                return ConfigureApp.Android.InstalledApp("com.companyname.trumpeldor").StartApp();
            }

            return ConfigureApp.iOS.StartApp();
        }
    }
}