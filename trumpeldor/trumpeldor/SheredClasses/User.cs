using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class User
    {
        //Has to be
        public string name { get; set; }
        public string socialNetwork { get; set; }
        public DateTime? lastSeen { get; set; }
        public String email { get; set; }
        //Maybe to get also if the user is connected recently because different customers will want different settings for that.

    }
}
