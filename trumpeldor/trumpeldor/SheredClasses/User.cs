using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class User
    {
        //Has to be
        internal string name { get; set; }
        internal string socialNetwork { get; set; }
        //internal List<string> playersAges { get; set; }
        internal DateTime? lastSeen { get; set; }
        internal string email { get; set; }
        //Maybe to get also if the user is connected recently because different customers will want different settings for that.

        //THIS CONSTRUCTOR IS FOR THE CONNECTION IMPORTANT!!!!!!!!!!!!!!!
        public User()
        {
        }

        public User(string name, string socialNetwork, DateTime? lastSeen, string email)
        {
            this.name = name;
            this.socialNetwork = socialNetwork;
            this.lastSeen = lastSeen;
            this.email = email;
        }
    }
}
