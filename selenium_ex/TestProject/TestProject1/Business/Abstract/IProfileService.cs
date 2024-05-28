using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject1.Business.Abstract
{
    public interface IProfileService
    {
        public void GetFollowing();
        public void GetFollowers();
    }
}
