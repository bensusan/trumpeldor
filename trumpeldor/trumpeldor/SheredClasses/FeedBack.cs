using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;


using Newtonsoft.Json;

namespace trumpeldor.SheredClasses
{
    class FeedBack
    {
        [JsonProperty("questions")]
        public String Question { get; set; }
    }
}


