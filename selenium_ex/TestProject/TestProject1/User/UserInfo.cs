﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject1.UserInfo
{
    public class UserInfo
    {
        public string Username { get; set; }
        public string Password { get; set; }
        public string FollowerName { get; set; }

        public UserInfo()
        {
            Username = "";
            Password = "";
            FollowerName = "";
        }
    }
}
