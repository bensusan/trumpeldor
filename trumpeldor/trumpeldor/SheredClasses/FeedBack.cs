using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Feedback
    {
        public int id { get; set; }
        public string question { get; set; }
        public string kind { get; set; }

        //not to use
        public enum Kinds { FeedBackRating = 1, FeedBackText = 2};

    }
}
