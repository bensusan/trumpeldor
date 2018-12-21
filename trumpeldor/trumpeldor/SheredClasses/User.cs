using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class User
    {
        public String name { get; set; }
        public String socialNetwork { get; set; }
        public List<String> playersAges { get; set; }
        public String lastSeen { get; set; }
        public String email { get; set; }
    }
}
