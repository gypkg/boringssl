{
  "targets": [{
    "target_name": "boringssl",
    "type": "<!(gypkg type)",

    "direct_dependent_settings": {
      "include_dirs": [ "src/include" ],
    },

    "includes": [ "boringssl.gypi" ],

    "include_dirs": [ "src/include" ],

    "sources": [
      "<@(boringssl_ssl_sources)",
      "<@(boringssl_crypto_sources)",
    ],

    "conditions": [
      [ "OS=='mac' and target_arch=='ia32'", {
        "sources": [ "<@(boringssl_mac_x86_sources)" ],
      }, "OS=='mac' and target_arch=='x64'", {
        "sources": [ "<@(boringssl_mac_x86_64_sources)" ],
      }, "OS=='win' and target_arch=='ia32'", {
        "sources": [ "<@(boringssl_win_x86_sources)" ],
      }, "OS=='win' and target_arch=='x64'", {
        "sources": [ "<@(boringssl_win_x86_64_sources)" ],

      # Linux and others
      }, "target_arch=='ia32'", {
        "sources": [ "<@(boringssl_linux_x86_sources)" ],
      }, "target_arch=='x64'", {
        "sources": [ "<@(boringssl_linux_x86_64_sources)" ],
      }, "target_arch=='arm'", {
        "sources": [ "<@(boringssl_linux_arm_sources)" ],
      }, "target_arch=='arm64'", {
        "sources": [ "<@(boringssl_linux_aarch64_sources)" ],
      }],
    ],
  }],
}
