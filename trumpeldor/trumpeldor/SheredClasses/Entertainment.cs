using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
    public abstract class Entertainment
    {
        public virtual int id { get; set; }

        public abstract string EntertainmentName();

        public abstract ContentPage EntertainmentPageInstance(ContentPage nextPage);
    }
}
