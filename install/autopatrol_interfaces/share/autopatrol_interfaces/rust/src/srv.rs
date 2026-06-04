#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to autopatrol_interfaces__srv__SpeachText_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpeachText_Request {
    /// 合成文字
    pub text: std::string::String,

}



impl Default for SpeachText_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SpeachText_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SpeachText_Request {
  type RmwMsg = super::srv::rmw::SpeachText_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        text: msg.text.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        text: msg.text.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      text: msg.text.to_string(),
    }
  }
}


// Corresponds to autopatrol_interfaces__srv__SpeachText_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpeachText_Response {
    /// 合成结果
    pub result: bool,

}



impl Default for SpeachText_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SpeachText_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SpeachText_Response {
  type RmwMsg = super::srv::rmw::SpeachText_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        result: msg.result,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      result: msg.result,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      result: msg.result,
    }
  }
}






#[link(name = "autopatrol_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__autopatrol_interfaces__srv__SpeachText() -> *const std::ffi::c_void;
}

// Corresponds to autopatrol_interfaces__srv__SpeachText
#[allow(missing_docs, non_camel_case_types)]
pub struct SpeachText;

impl rosidl_runtime_rs::Service for SpeachText {
    type Request = SpeachText_Request;
    type Response = SpeachText_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__autopatrol_interfaces__srv__SpeachText() }
    }
}


