export const environment = {
  production: false,

  OPENAI_API_KEY: "",

  temperature: 0.0,
  max_tokens: 400,
  top_p: 1,
  frequency_penalty: 0,
  presence_penalty: 0,
  pretext: '/*\n',
  posttext: '\n*/\nImplementation in C:\n',

  nl_temperature: 0.0,
  nl_max_tokens: 100,
  nl_top_p: 1,
  nl_frequency_penalty: 0,
  nl_presence_penalty: 0,
  nl_pretext: '',
  nl_posttext: 'Short Explanation of the code above:',
};
