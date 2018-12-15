﻿using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;

namespace trumpeldor
{
    class ServerConection
    {
        private readonly String urlPrefix = "http://192.168.1.9:12345/";
        public ServerConection()
        {

        }

        public List<TrackPoint> SelectPath(GameController.PathLength selectedPathLength)
        {
            //track point contain only id,Latitude,Longitude,name
            return new List<TrackPoint>()
            {
                new TrackPoint(31.262485, 34.803953),
                new TrackPoint(31.261930, 34.804132)
                
            };
            //TODO
        }
        public TrackPoint GetTrackPointById(string id)
        {
            //track point with all information
            return new TrackPoint(31.262485, 34.803953);
            //TODO
        }
        public List<Clue> GetTrackPointClues(string id)
        {
            return new List<Clue>();
            //TODO
        }
        public Game GetTrackPointGame(string id)
        {
            return new AQ();
            //TODO
        }
        public Game GetTrackPointAmericanQuestion(string id)
        {
            return new AQ();
            //TODO
        }

        public String GetGeneralInformation()
        {

            //TODO
            return "some general information";
        }



        /////
        ///

        public async Task getFeedbackAsync()
        {
            Task<String> result = resultGetAsync(urlPrefix + "feedback/");
            var posts = JsonConvert.DeserializeObject<List<FeedBack>>(await result);
        }

        public async Task signUp(String userEmail, List<String> playersAges, String name)
        {
            using (var client = new HttpClient())
            {
                // Create a new post  
                var newUser = new User
                {
                    Email = userEmail,
                    PlayersAges = playersAges,
                    Name = name
                };


                var content = contentPost(newUser);

                //  send a POST request  
                var uri = urlPrefix + "signUp/";
                var result = await client.PostAsync(uri, content);

                // on error throw a exception  
                result.EnsureSuccessStatusCode();

                // handling an answer maybe in the future  

            }
        }


        public async Task<String> resultGetAsync(String uri)
        {
            using (var client = new HttpClient())
            {
                return await client.GetStringAsync(uri);
            }
        }

        public StringContent contentPost(Object obj)
        {
            var json = JsonConvert.SerializeObject(obj);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            return content;
        }
    }
}
