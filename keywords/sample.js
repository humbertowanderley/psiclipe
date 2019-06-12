//  include the Keyword Extractor
var keyword_extractor = require("./lib/keyword_extractor");

var sentence = "missing you Saying this makes me miss you even more I am looking at your photo Time is so cruel, I hate us Seeing each other for once is now so hard between us"

//  Extract the keywords
var extraction_result = keyword_extractor.extract(sentence,{
                                                                language:"english",
                                                                remove_digits: true,
                                                                return_changed_case:false,
                                                                remove_duplicates: true

                                                           });
console.log(extraction_result);

