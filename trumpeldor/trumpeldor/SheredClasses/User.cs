﻿using System;
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

        public enum SOCIAL_NETWORK { Google, Facebook/*, Instegram*/, Anonymous}
        public static Dictionary<SOCIAL_NETWORK, string> SocialNetwork2string = new Dictionary<SOCIAL_NETWORK, string>()
        {
            { SOCIAL_NETWORK.Google, "google" },
            { SOCIAL_NETWORK.Facebook, "facebook" },
            //{ SOCIAL_NETWORK.Instegram, "instegram" },
            { SOCIAL_NETWORK.Anonymous, "" }
        };
    }
}
