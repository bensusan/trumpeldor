using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;


using Newtonsoft.Json;

namespace trumpeldor.SheredClasses
{
    public class FeedbackInstance
    {
        public int id { get; set; }
        public Feedback feedback { get; set; }
        public string answer { get; set; }
    }
}


