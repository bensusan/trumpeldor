﻿using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.Views;
using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
    public class TakingPicture : Entertainment
    {
        public override string EntertainmentName()
        {
            return AppResources.taking_picture;
        }

        public override ContentPage EntertainmentPageInstance(ContentPage nextPage)
        {
            return new TakingPicturePage(this, nextPage);
        }

        public static bool isMyClassName(string className)
        {
            return "TakingPicture".Equals(className);
        }
    }
}
