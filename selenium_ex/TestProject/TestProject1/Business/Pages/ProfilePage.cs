using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject1.Pages
{
    public class ProfilePage
    {
        public readonly IWebDriver _driver;

        public ProfilePage(IWebDriver driver)
        {
            _driver = driver;
        }
        public IWebElement ThirdLiElement => _driver.FindElement(By.CssSelector("ul.x78zum5 li:nth-child(3)"));
        public IWebElement SecondLiElement => _driver.FindElement(By.CssSelector("ul.x78zum5 li:nth-child(2)"));
        public IWebElement GetFollowerSearchButton => _driver.FindElement(By.CssSelector("input[aria-label='Arama Girdisi']"));


    }
}
