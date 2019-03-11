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

        public enum Kinds {FeedBackRating, FeedBackText};
        public static Dictionary<string, Kinds> kindToEnum = new Dictionary<string, Kinds>
            {
                {"FT", Kinds.FeedBackText },
                {"FR", Kinds.FeedBackRating }
            };

    }
}
