using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Xamarin.Forms;

namespace trumpeldor.SheredClasses
{
	public class AmericanQuestion
    {
        public int id { get; set; }
        public string question { get; set; }
        public List<string> answers { get; set; }
        public int[] indexOfCorrectAnswer { get; set; }

    }
}