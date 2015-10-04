$userLogin = 'EnterSandboxLogin'
$userPass = 'EnterSandboxPass'

Given /^I am on the Welcome Screen$/ do
  element_exists("* marked:'Authenticate'")
end

Given /^I should see login screen$/ do
  if query("webView css:'*'").empty? == false
    sleep (5) #Should be wait_for_element_exists function
  end
end

Given /^I scroll down to Password field$/ do
    for i in 0..5
      scroll("UIWebView", :down)
    end
end

Given /^I enter my credentials$/ do
  css_elements = query("webView css:'*'")

  touch css_elements[28] #Login field. Hardcoded for now, should be a css label
  sleep (2) #wait to keyboard appears
  keyboard_enter_text("#{$userLogin}")

  touch css_elements[32] #Password field. Hardcoded for now, should be a css label
  sleep (2)
  keyboard_enter_text("#{$userPass}")
end

Given /^I press Sign In button$/ do
  tap_keyboard_action_key
end

Given /^I authorize app$/ do
  sleep (5)
  css_elements = query("webView css:'*'")
  touch css_elements[55] #Re-authorize btn. Hardcoded for now, should be a css label
end

Given /^I going to login$/ do
  element_exists("* marked:'Authenticate'")
  macro ("I touch the \"Authenticate\" button")
  macro ("I wait for 2 seconds")
  if query("webView css:'*'").empty? == false
    sleep (5) #Should be wait_for_element_exists function
  end
  for i in 0..5
    scroll("UIWebView", :down)
  end
  css_elements = query("webView css:'*'")

  touch css_elements[28] #Login field. Hardcoded for now, should be a css label
  sleep (2) #wait to keyboard appears
  keyboard_enter_text("#{$userLogin}")

  touch css_elements[32] #Password field. Hardcoded for now, should be a css label
  sleep (2)
  keyboard_enter_text("#{$userPass}")
  tap_keyboard_action_key
  sleep (5)
  css_elements = query("webView css:'*'")
  touch css_elements[55] #Re-authorize btn. Hardcoded for now, should be a css label
  macro ("I wait to see \"Evernote SDK\"")
end